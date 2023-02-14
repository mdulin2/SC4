#include<stdio.h>
#include<signal.h>
#include<unistd.h>
#include <math.h>

// Defaults to ALL zeros
int games[0x100]; 

int high_score; // High score for the current user

/*
Handle an interrupt to start a new game
*/
void sig_handler(int signum){

	//Return type of the handler function should be void
	start(1); 
}


/*
Press the buttons and save your scores!
*/
void play(int current_button_count, int user_no){
	int counter = current_button_count; 

	while(1){
		int option = get_option(); 

		// Press button
		if(option == 1){
			puts("Pressed button! Dopemine hit!"); 
			counter += 1; 
			sleep(1); 
		}
		else if(option == 2){
			save_game(user_no, counter);
		}
		else if(option == 3){
			printf("Score: %d\n", games[user_no]); 
			if(games[user_no] > high_score){
				get_flag();
			}
		}else if(option == 4){
			puts("Byte bye!"); 
			return; 
		}
	}
	
}

// Get option for playing
int get_option(){
	printf("1. Press button!\n"); 
	printf("2. Save Game\n");
	printf("3. Check score\n"); 
	printf("4. Exit\n"); 
	printf("> "); 

	char tmp[20];
	
	fgets(tmp,10,stdin);
	return atoi(tmp);
}

// Print the flag
void get_flag(){
    FILE *fp; 
    int c; 
    fp = fopen("flag.txt","r");

	printf("Flag: "); 
    // Read the output of the flag file    
    if(fp){
        while((c = getc(fp)) != EOF)
    		putchar(c); 
        fclose(fp);

    } else {
          puts("Unable to read flag");
	}
}

// Display the title screen info
int title_screen(){

	char line[128];
	int attempt = 0; 

	printf("Enter save file slot to use: "); 
	while(1){
		if(fgets(line, sizeof(line), stdin) == NULL){
			break;
		}

		// Convert string to int
		attempt = strtol(line, NULL, 10);
		if(attempt >= 0 && attempt < 0x100){
			return attempt;
		}	
	}
}

// 
int load_save(int slot){
	return games[slot];
}

/*
Store the user game for later
*/
int save_game(int slot, int value){

	// Set the slot to all 1s
	puts("Clearing previous game...");
	games[slot] = pow(2, 32) - 1; 

	// Set the writes cool off
	sleep(2);

	// Set the real score
	puts("Saving current game...");
	games[slot] = value; 

	return slot; 
}

// The main loop for the game
void start(int first){

	// Loop until we want to stop
	while(1){

		if(first != 0){
			puts("Type 'y' to exit game. Press anything else to continue."); 
			char tmp[20];
			fgets(tmp,10,stdin);
			if(tmp[0] == 'y'){
				exit(0);
			}
		}

		// Load the save game
		int slot = title_screen(); 

		// Get the previous save file
		int counter = load_save(slot);

		// Play the game
		play(counter, slot); 
	}
	return 0;
}


// Starting point
int main(){
	high_score = pow(2,30); // Set the high score
	signal(SIGINT,sig_handler); // Register signal handler for interrupt
	start(0); 
}

