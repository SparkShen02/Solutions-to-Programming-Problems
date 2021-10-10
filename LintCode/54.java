public class Solution{
  public static int atoi(String str){
    if(str.length()==0){return 0;}
    String num="0123456789";
    String sign="+-";
    int judge=0;
    int count=0;
    String string="";
    String chara="";
    for(int i=0;i<str.length();i++){
      chara=str.substring(i,i+1);
      if(judge==0){
        if(num.contains(chara)||sign.contains(chara)){
          string+=chara;
          if(!(sign.contains(chara))){count+=1;}
          judge+=1;
          continue;
        }
        else if(!(chara.equals(" "))){return 0;}
        else{continue;}
      }
      if(num.contains(chara)){string+=chara; count+=1;}
      else{break;} 
    }
    return result(count,string,str,sign);
  }
  
  public static int result(int count,String string,String str,String sign){
    if(string.equals("+") || string.equals("-")){return 0;}
    if(count>10){
      if(string.substring(0,1).equals("-")){return -2147483648;}
      return 2147483647;
    }
    if(count==10){
      String max="2147483647";
      String min="-2147483648";
      if(string.substring(0,1).equals("-")){
        for(int i=1;i<str.length();i++){
          String curr=string.substring(i,i+1);
          String samp=min.substring(i,i+1);
          if(Integer.parseInt(curr)<Integer.parseInt(samp)){return Integer.parseInt(string);}
          if(Integer.parseInt(curr)>Integer.parseInt(samp)){return -2147483648;}
        }
      }
      else{
        for(int i=0;i<str.length();i++){
          if(sign.contains(string.substring(0,1))){i+=1;}
          String curr=string.substring(i,i+1);
          String samp=max.substring(i,i+1);
          if(Integer.parseInt(curr)<Integer.parseInt(samp)){return Integer.parseInt(string);}
          if(Integer.parseInt(curr)>Integer.parseInt(samp)){return 2147483647;}
        }
      }
    }    
    return Integer.parseInt(string);
  }
}