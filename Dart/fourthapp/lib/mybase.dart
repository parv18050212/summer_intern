import 'package:flutter/material.dart';
import 'package:fouthapp/mybody.dart';

class MyApp1 extends StatelessWidget {
  const MyApp1({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.pinkAccent,
        ),
        body: Mybodoy1(),
      ),
    );
  }
}
