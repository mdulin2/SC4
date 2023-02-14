// Modifed from https://www.geeksforgeeks.org/tcp-server-client-implementation-in-c/
// gcc server.c -o server
#include <netdb.h> 
#include <stdio.h>
#include <netinet/in.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <sys/types.h> 
#include <unistd.h>
#include <ctype.h>
#include <time.h>

#define MAX 80 
#define SA struct sockaddr 

// Really ensures that the values are the same. 
int sure_equals(char ch, char ch2){
	if(ch != ch2){
		return 0; 
	}
	sleep(1); 	
	return 1; 
}

// Does the user have the right password? 
int check_auth(char *attempt, char *password){
	
	// Check the length to match.
	if(strlen(attempt) != strlen(password)){
		printf("Not enough characters...\n");
		return 0; 
	}
	
	// Iterates over each character in the array.
	for (int index = 0; index < strlen(password); index ++){
		int result = sure_equals(password[index], attempt[index]);
		
		// If the attempt is wrong, then exit. 
		// This is fast to return earlier! :)
		if(result == 0){
			return 0; 
		}
	}
	return 1;
}

// Function designed for chat between client and server. 
void login_wrapper(int sockfd) 
{ 
	
    char password[MAX]; 
    int n; 
	
	// Clear the memory 
	bzero(password, MAX);
	
	// Read the password from the client 
    read(sockfd, password, MAX); 	

	// The flag! 
	char *pin = "140329823";
	int answer = check_auth(password, pin);
	
	// Send flag or not the flag. 
	char* result; 
	if(answer == 1){
		result = "Correct";
	}
	else{
		result = "Invalid"; 
	}
	write(sockfd, result, strlen(result)); 
	return;
} 
  
//\\\//\\\ Ignore this! //\\//\\//
int main(int argc, char* argv[] ) 
{ 
	// 1st parameter should be the port...
	int PORT = atoi(argv[1]);
    int sockfd, connfd, len; 
    struct sockaddr_in servaddr, cli; 
  
    // socket create and verification 
    sockfd = socket(AF_INET, SOCK_STREAM, 0); 
    if (sockfd == -1) { 
        printf("socket creation failed...\n"); 
        exit(0); 
    } 
    else
        printf("Socket successfully created..\n"); 
	
    bzero(&servaddr, sizeof(servaddr)); 
  
    // assign IP, PORT 
    servaddr.sin_family = AF_INET; 
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY); 
    servaddr.sin_port = htons(PORT); 
  
    // Binding newly created socket to given IP and verification 
    if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) { 
        printf("socket bind failed...\n"); 
        exit(0); 
    } 
    else
        printf("Socket successfully binded on port %d\n",  PORT); 
  
    // Now server is ready to listen and verification 
    if ((listen(sockfd, 5)) != 0) { 
        printf("Listen failed...\n"); 
        exit(0); 
    } 
    else
        printf("Server listening..\n"); 
		len = sizeof(cli); 
  
	while(1){
		// Accept the data packet from client and verification 
		connfd = accept(sockfd, (SA*)&cli, &len); 
		if (connfd < 0) { 
			printf("server acccept failed...\n"); 
			exit(0); 
		} 
		else
			printf("server acccept the client...\n"); 

 		/*
        Fork.
        - Parent: Accept more connections
        - Child: Process and continue with the current request by entering 'login_wrapper'
        */ 
        if(fork() == 0){
            close(sockfd);

			// Function for chatting between client and server 
			login_wrapper(connfd); 
			close(connfd);
			exit(0);
		}

		close(connfd);

	}
	
	close(sockfd); 
} 
