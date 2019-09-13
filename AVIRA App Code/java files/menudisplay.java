package com.example.aksha.avira;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.view.View;
/**
 * Created by aksha on 19-03-2018.
 */

public class menudisplay extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.menudisplay);
        final String but_on="restart";
        final String shut = "shutdown";
        final Button button = (Button) findViewById(R.id.brestart);
        final Button shutdown_but = (Button) findViewById(R.id.bshutdown);
        Button micBtn = (Button) findViewById(R.id.bmic);

        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Code here executes on main thread after user presses button
                new Socket_connection().execute(but_on);
            }
        });

        shutdown_but.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Code here executes on main thread after user presses button
                new Socket_connection().execute(shut);
            }
        });

        micBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                gotovoice();
            }
        });

    }

    public void gotovoice()
    {
        Intent j = new Intent(menudisplay.this, voicetotext.class);
        startActivity(j);
    }

}

