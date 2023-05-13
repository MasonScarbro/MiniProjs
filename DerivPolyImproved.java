package polysolveD;

import java.util.ArrayList;
import java.util.*;

public class DerivPolyImproved {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("WELCOME TO THE DERIVATIVE SOLVER FOR POLYNOMIALS \n" + "! FRACTIONS CANNOT BE HANDLED... YET !");
		System.out.println("Please Enter the PolyNomial with no spaces");
	    String polynomial = input.next();
	    
	    // replaces the - sign with a + so i can still split by + 
	    polynomial.replace("-", "+-");
		String[] parts = polynomial.split("\\+");
		ArrayList<String> partsList = new ArrayList<>(Arrays.asList(parts));
		ArrayList<String> coefficients = new ArrayList<>();
		ArrayList<String> exponent = new ArrayList<>();
		ArrayList<String> single = new ArrayList<>();
		
		for (int i = partsList.size() - 1; i >= 0; i--) {
			// creates a part to make loops easier
			String part = partsList.get(i);
			// automatically removes anything without an x
			if (!part.contains("x")) {
				partsList.remove(i);
			}else if (part.contains("^") == false) {
				single.add(part);
				partsList.remove(i);
			} else {
				// adds all the coefficients to the coefficients array list
				coefficients.add(partsList.get(i).substring(0, partsList.get(i).indexOf("x")));
				// adds all the expontents to the exponents arrat list
				exponent.add(partsList.get(i).substring(partsList.get(i).indexOf("^") + 1, partsList.get(i).length()));
				
			}
	 	
		}
		// can be expontents or coefficients since they will always be equal to each other
		for (int j = 0; j < exponent.size(); j++) {
			
			// makes the new coefficient and exponent and changes the values of the partsList array
			int newCoefficient = Integer.parseInt(coefficients.get(j)) * Integer.parseInt(exponent.get(j));
			int newExponent = Integer.parseInt(exponent.get(j)) - 1;
			partsList.set(j, newCoefficient + "x" + "^" + newExponent);
		}
		// creates new derivate var without the + C
		String derivativeAlmost = "";
		// creates the C variable (not sure why i called it single, looking back it would make more sense for it to be c)
		String singleL = single.get(0).replace("x", "");
		// loop reversing (reversed earlier and concatenating the function/derivative without the C
		for (int k = partsList.size() - 1; k >= 0; k--) {
			derivativeAlmost += partsList.get(k) + "+";
		
		}
		// checks if single has more than one number if it does it will add them so they are one number
		if (single.size() >= 2) {
			int singleInt = Integer.parseInt(singleL);
			for (int n = 0; n < single.size(); n++) {
				singleInt += Integer.parseInt(single.get(n).replaceAll("x", ""));
			}
			singleL = Integer.toString(singleInt);
		} else {/*empty*/}
		// checks if any +- is in the final function so it can just make it '-' (easier to read)
		if (derivativeAlmost.indexOf("+-") != -1) {
			derivativeAlmost = derivativeAlmost.replaceAll("+-", "-");
		}
		else {/*empty*/}
		// checks if any part has a ^1 since thats just #x 
		if (derivativeAlmost.indexOf("^1") != -1) {
			derivativeAlmost = derivativeAlmost.replace("^1", "");
		} else {/*empty*/}
		// once again checks if it has a useless exponent and fixes it accordingly
		if (derivativeAlmost.indexOf("^0") != -1) {
			derivativeAlmost = derivativeAlmost.replace("x^0", "");
		}
		
		
		System.out.println(derivativeAlmost + singleL);
		
	}

}
// NOTES: Gonna have to use the iterator since right now its going backwards and screwing up the order of things
// For the final string try string += string so partsList.get(i) += partsList.get(i) sort of
// if their are more than one exponent single like 6x make sure it add them before
// try changing the parts list to match the new exponents and numbers by using the set method