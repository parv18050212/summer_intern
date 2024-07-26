import 'package:flutter/material.dart';

lw() {
  print("hi this is clicked");
}

main() {
  runApp(MaterialApp(
    home: Scaffold(
      floatingActionButton: FloatingActionButton(
        onPressed: null,
      ),
      body: Text("Linux World"),
      appBar: AppBar(
        actions: [IconButton(onPressed: lw, icon: Icon(Icons.add_call))],
        backgroundColor: Color.fromARGB(255, 239, 26, 26),
        title: Text("Linux World App"),
        centerTitle: true,
        leading: Icon(
          Icons.add_a_photo,
          color: Colors.green[200],
          size: 36.0,
        ),
      ),
    ),
  ));
}
