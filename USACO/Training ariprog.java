/* Use the slash-star style comments or the system won't see your
 identification information */
/*
 ID: shenyu01
 LANG: JAVA
 TASK: ariprog
 */
import java.io.*;
import java.util.*;

class ariprog{
  public static void main (String [] args) throws IOException {
    BufferedReader f = new BufferedReader(new FileReader("ariprog.in"));
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("ariprog.out")));
    
    int length = Integer.parseInt(f.readLine());  
    int upper = Integer.parseInt(f.readLine());   
    
    //findBisquares
    boolean[] bisquares = new boolean[2*upper*upper+1];
    for(int i=0; i<bisquares.length; i++){
      bisquares[i] = false;
    }
    for(int i=0; i<=upper; i++){
      for(int j=0; j<=upper; j++){
        int num = i*i + j*j;
        bisquares[num] = true;
      }
    }
    
    //findProgressions
    boolean if_none = true;
    for(int b=1; b<=(int)(upper*upper*2 / (length-1)); b++){
      for(int a=0; a<=upper*upper*2 - b*(length-1); a++){
        if (bisquares[a] == false) 
          continue;
        boolean judge = true;
        for(int n=0; n<length; n++){
          if (bisquares[a+n*b] == false){
            judge = false;
            break;
          }
        }
        if (judge == true){
          String str = Integer.toString(a) + ' ' + Integer.toString(b);
          if_none = false;
          out.println(str);
        }
      }
    }
    
    if (if_none)
      out.println("NONE");
    
    out.close();                                 
  }
}