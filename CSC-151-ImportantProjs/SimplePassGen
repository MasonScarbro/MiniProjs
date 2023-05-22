// A Simple but effective Java Program that generates a password with 1e to the something power different possibilities (basically infinite) 
import java.util.Scanner;
public class PasswordGenerator {
	
	/** 
	 * Special characters 
	 *
	 * @return Returns n array of chars containing all valid special characters
	 */
	public static char[] getSpecialCharacters() {
		final char[] SPECIAL_CHARS = {'!', '@', '#', '_', '.', '*'};
		return SPECIAL_CHARS;
	}
	
	/** 
	 * Valid password characters 
	 *
	 * @return Returns String containing all valid password characters
	 */
	public static final String getValidPasswordCharacters() {
		final String PASSWORD_CHARS = "abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVEWXYZ0123456789";
		return PASSWORD_CHARS;
	}
	
	/** 
	 * @return Returns a single String of 140 four-letter words than can be used in a password.
	 * 
	 */
	public static final String getAllFourLetterWords() {

		final String FOUR_LETTER_WORDS =
			"able bane barn bile blip boat bolt bran brat brim bulb "+
			"bull burn cane card cart clan clip cold cone core dart "+
			"deny dial dang dirk dolt door dote drip drop dupe each "+
			"earn easy fast fest file five flap flip flop foal folk "+
			"fort four full gave give gone grin hard hurt idle isle "+
			"join king knit knob land lane lard link list live long "+
			"lung made main many mile mine moat mole mote mule nine "+
			"norm note paid part pick pile ping pipe plan pole pong "+
			"port prim pull quid quip quit rain rang redo ring ripe "+
			"role root rote rung sand sang silk sing sink slam slow "+
			"song sort spam sulk take tame tang tide tile time tint "+
			"toll tone took tote trap trip turn undo vile volt vote "+
			"wart wing woke wool wore writ zero zoom";
	   return FOUR_LETTER_WORDS;
	}

	
	
	/** 
	 * Create a password 
	 * 
	 * @return Returns a password meeting all of the specifications
	 */
	public static String createPassword() {
		
	

		String[] fourWords = new String[140];
		int firstIndex = 0;
		int secondIndex = 4;
		int randoLetta = (int)(Math.random() * 140);
		String randomFourWord;
		
			    for (int i = 0; i < 140; i++) {
			    	fourWords[i] = getAllFourLetterWords().substring(firstIndex, secondIndex);
			    	firstIndex += 5;
			    	secondIndex += 5;
			    	
			    }
			    randomFourWord = fourWords[randoLetta];
			    // converts the return from the other method to a usable array
			    char[] specialChars = getSpecialCharacters();
			    // chooses any of the 6 special characters at random
			    char specChara = specialChars[(int)(Math.random() * 6)];
			    // grabs random digits and makes sure that if below 10 an 0 is added
			    int randomDigit = (int)(Math.random() * 100);
			    String randoDigi;
			    		if (randomDigit < 10) {
			    			randoDigi = "0" + String.valueOf(randomDigit);
			    		} else {
			    			randoDigi = String.valueOf(randomDigit);
			    		}
			    		
			    		String[] randomWords = new String[getValidPasswordCharacters().length()];
			    		// sorts the randomWords array so it can grab each and every character 
			    			for (int j = 0; j < getValidPasswordCharacters().length(); j++ ) {
			    				randomWords[j] = getValidPasswordCharacters().substring(j, j + 1);
			    			}
			    			// grabs 5 random word/nums form the array and adds them to one string
			    			String randomWord1 = randomWords[(int)(Math.random() * 62)];
			    			String randomWord2 = randomWords[(int)(Math.random() * 62)];
			    			String randomWord3 = randomWords[(int)(Math.random() * 62)];
			    			String randomWord4 = randomWords[(int)(Math.random() * 62)];
			    			String randomWord5 = randomWords[(int)(Math.random() * 62)];
			    			String randomWordTotal = randomWord1 + "" + randomWord2 + "" + randomWord3 + "" + randomWord4 + "" + randomWord5;
			    			
			    
			    			String password = randomFourWord + "" + specChara + "" + randoDigi + "" + randomWordTotal;
	 
		
		return password; 
	}

	/** 
	 * Return true if this password is unique to the list of generated passwords.  
	 */	
	public static boolean isPasswordUnique(String aPassword, String passwordList) {
		String [] passwordS = passwordList.split(" "); // splits the password list into an array assuming each password is slpit by a space
		
		// a for each loop that check for each password in the list if it equals the password entered
		for(String password : passwordS) {
			if (password.equals(aPassword)) {
				return false;
			}
		}
		return true;
	}
	
	/**
	 * Add aPassword to the list of unique passwords
	 * 
	 * @param aPassword: the password to add
	 * @param passwordList: A string containing all unique passwords, separated by spaces
	 * @return Updated passwordList with the new password
	 */
	public static String addUniquePassword(String aPassword, String passwordList) {
		
		if (isPasswordUnique(aPassword, passwordList)) {
			if (passwordList.isEmpty()) {
				return aPassword; // it will be empty at first so the first pass will be unique
			} else {
				return passwordList + " " + aPassword; // returns password list with the new unique password added on
			}
		} else {
			return passwordList; // if its not unique just return the list do not add
		}
		
	}
	
	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		System.out.print("How many passwords do you want to generate? ");
		int numPasswords = scanner.nextInt();
		scanner.close();
		
		
		String uniquePasswords = ""; // that password list we were talking about earlier
		
		// a for loop designed to iterate through each time that the person needs a password
		for (int i = 0; i < numPasswords; i++) {
		 
			String newPassword = createPassword(); // creates a new password for each iteration
			// checks if each new password is unique
			if (isPasswordUnique(newPassword, uniquePasswords)) {
				// if it is then it adds a new unique password to the list
				uniquePasswords = addUniquePassword(newPassword, uniquePasswords);
				System.out.println(newPassword); 
			}
		}
	}
}
