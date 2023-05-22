package DerivativePoly;

import java.util.Scanner;
import java.util.*;
import java.math.*;

public class DerivPolyAbs {

	public static void main(String[] args) {
	
		String poly;
		Scanner kbyd = new Scanner(System.in);
		System.out.println("Enter Your PolyNomial With No Spaces and no double digit exponents:");
		poly = kbyd.nextLine();
		int first = poly.indexOf("^");
		int firstB = Integer.parseInt(poly.substring(first + 1, first + 2));
		int firstA = Integer.parseInt(poly.substring(0, first - 1));
		
		String middleStr = poly.substring((poly.indexOf("^") + 1), poly.length());
		int middleStrB = Integer.parseInt(middleStr.substring((middleStr.indexOf("^") + 1), (middleStr.indexOf("^") + 2)));
		int middleStrA = Integer.parseInt(middleStr.substring(middleStr.indexOf(firstB) + 2,middleStr.indexOf("^") - 1));
	
		
		 String pastC = middleStr.substring(middleStr.indexOf("^") + 2,middleStr.length());
	
		 
		
		if (pastC.indexOf("^") > -1) {
			System.out.println("Hey You Might Not Know What A Polynomial Is! Thats Okay the correct answer will still be displayed");
			int pastFirstcB = Integer.parseInt(pastC.substring(pastC.indexOf("^") + 1, pastC.length()));
			int pastFirstcA = Integer.parseInt(pastC.substring(pastC.indexOf(middleStrB) + 2,pastC.indexOf("^") - 1));
			int c = pastFirstcA * pastFirstcB;
			String derC = Integer.toString(c) + "x" + "^" + Integer.toString(pastFirstcB - 1); 
			
			
		} else {
			 
			String derA = Integer.toString(firstA * firstB);
			String derB = Integer.toString(firstB - 1);
			
			String inF = poly.substring(poly.indexOf("^") + 2,poly.indexOf("^") + 3);
			
			String derA2 = Integer.toString(middleStrA * middleStrB);
			String derB2 = Integer.toString(middleStrB - 1);
			
			String derC = pastC.substring(pastC.indexOf("x") - 1, pastC.indexOf("x"));
			String fPrime = derA + "x" + "^" + derB + inF + derA2 + "x" + "^" + derB2 + middleStr.substring(middleStr.indexOf("^") + 2 ,middleStr.indexOf("^") + 3) + derC; 
			System.out.println(fPrime);
			
			
			
			
			
		}
		

	} 
	
}
