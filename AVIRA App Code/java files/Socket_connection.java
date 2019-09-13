/**
 * Created by aksha on 01-05-2018.
 */
package com.example.aksha.avira;

import android.os.AsyncTask;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;




public class Socket_connection extends AsyncTask <String,Void,Void> {
    private Exception exception;


    @Override
    protected Void doInBackground(String... params) {
        try {

            try{

                Socket socket = new Socket("192.168.43.116",9999);

                PrintWriter outToServer = new PrintWriter(new OutputStreamWriter(socket.getOutputStream()));

                outToServer.print(params[0]);
                outToServer.flush();


            }
            catch (IOException e){

                e.printStackTrace();
            }

        }
        catch (Exception e){

            this.exception = e;



        }
        return null;
    }
}

