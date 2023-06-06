import java.io.*;
import java.security.*;
import javax.crypto.*;

// java Main -genkey keyFile generates key for encryption args[0]
// java Main -encrypt plaintext encrypted keyFile- encrypts data first arg args[1] and args[2]
// java main -decrypt encrypted decrypted keyFile  args[3]

public class Main {
  public static void main(String[] args) throws IOException, ClassNotFoundException, GeneralSecurityException {
    if (args[0].equals("-genKey")){
    KeyGenerator keyGenerator = KeyGenerator.getInstance("AES"); // Java.security class that calls and create a random key using the AES encrytpion method
    SecureRandom random = new SecureRandom(); // more secure than Random
    keyGenerator.init(random); // initializes the random in the keyGen
    SecretKey key = keyGenerator.generateKey(); // calls generate key and generates a random key
    var out = new ObjectOutputStream(new FileOutputStream(args[1]));
    try{
      out.writeObject(key);
    }catch(Exception e){}
      
    }else{ // We do either encryption or decryption
      int mode;
      if (args[0].equals("-encrypt")){
        mode = Cipher.ENCRYPT_MODE;
      } else { // "-decrypt"
        mode = Cipher.DECRYPT_MODE;
      }

      var keyIn = new ObjectInputStream(new FileInputStream(args[3])); // keyFile
      var in = new FileInputStream(args[1]);
      var out = new FileOutputStream(args[2]);
      var key = (Key) keyIn.readObject(); // actually reads the file prev was an object

      Cipher cipher = Cipher.getInstance("AES");
      cipher.init(mode, key);
      Util.crypt(in, out, cipher); // pass in then out using cipher
    }
  }
}