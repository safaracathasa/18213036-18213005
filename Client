import java.lang.*;
import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    private static Socket socket;
   public static void main(String args[]) {
      String serverName = (args[0]);
      int portnum = Integer.parseInt(args[1]);
      
      try {
         System.out.println ("try to connect" + serverName + "at port" + portnum);
         Socket socket = new Socket(serverName, portnum);
         
         //send msg
         OutputStream os = socket.getOutputStream();
         OutputStreamWriter osw = new OutputStreamWriter(os);
         BufferedWriter bw = new BufferedWriter(osw);
         
         System.out.print("Message : ");
         Scanner in = new Scanner (System.in);
         String add = in.nextLine();
         
         bw.write(add);
         bw.flush();
         System.out.println ("Msg send :" +add);
         
         
         
         //receive msg
         InputStream is = socket.getInputStream();
         InputStreamReader isr = new InputStreamReader(is);
         BufferedReader ins = new BufferedReader(isr);
         String mg = ins.readLine();
         System.out.print("Received msg: '");

      }
      catch(Exception e) {
          e.printStackTrace();
         System.out.print("Whoops! It didn't work!\n");
      }
      finally
      {
          //closing
          try
          {
              socket.close();
          }
          catch (Exception exp)
          {
              exp.printStackTrace();
          }
      }
      
   }
}
