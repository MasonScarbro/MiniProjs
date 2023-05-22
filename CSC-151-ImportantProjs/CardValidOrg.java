/* Simple CreditCard number checker that checks if a credit card entered is a Valid card number or not based on regulations and rules. 
Alternatively this could also probably be tweaked so that instead of entering a password it generates one and checks if its valid. */
import java.util.Scanner;

public class cardvalidornot {
	/* @isValid: checks if teh card is valid by taking in the seperate functions
	 * @getPrefix: gets what ever the prefix of the number the card is 
	 * @prefixMatched: boolean that checks weather or not the prefix matches
	 * @getDigit: gets the digit associated with and needed for each sumOf function
	 * @sumOf: both take the sum of the digits using the get digit function and 
	 * their associated requirements such as double and even only and all odd nums
	 * @getSize: converts the long to string variable in order to get the size in 'length' of the long
	 */

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter a valid card number:");
        long number = input.nextLong();
        input.close();
        if (isValid(number)) {
            System.out.println("VALID!");
        } else { 
            System.out.println("NOT VALID");
        }
    }
		public static boolean isValid(long number) {
			boolean boo;
			boo = false;
			int sum = sumOfOddPlace(number) + sumOfEvenPlace(number);
			if (sum % 10 == 0) {
				if (prefixMatched(number, 37)){
					boo = true;
				}
				if (prefixMatched(number, 4)) {
					boo = true;
				}
				if (prefixMatched(number, 5)) {
					boo = true;
				}if (prefixMatched(number, 6)) {
					boo = true;
				}
			}
			return boo;
		}
		
		public static int sumOfEvenPlace(long number) {
			int sum = 0;
			String numStr = Long.toString(number);
			for (int i = numStr.length() - 2; i >= 0; i -= 2) {
				int doubleValue = Character.getNumericValue(numStr.charAt(i)) * 2;
				sum += getDigit(doubleValue);
			}
			return sum;
		}
		
		public static int getDigit(int number) {
			if (number < 10) {
				return number;
				
			}else {
				return number / 10 + number % 10;
			}
		}
		
		public static int sumOfOddPlace(long number) {
			int sum = 0;
			String numStr = Long.toString(number);
			for (int i = numStr.length() - 1; i >=0; i-= 2) {
				sum += Character.getNumericValue(numStr.charAt(i));
			}
			return sum;
		}
		
		public static boolean prefixMatched(long number, int d) {
			if (getPrefix(number, getSize(d)) == d)
			{
				return true;
			}else {
				return false;
			}
		}
		
		public static int getSize(long d) { 
				String numStr = Long.toString(d);
				return numStr.length();
		}
		   
		public static long getPrefix(long number,int k) {
			
			if (getSize(number) < k)
			{
				return number;
			}else {                     
				String numStr = Long.toString(number); /* converts number to string */
				return Long.parseLong(numStr.substring(0, k)); /* finds the numbers from 0 to k and converts back to long */
			}
			
		}

	}


