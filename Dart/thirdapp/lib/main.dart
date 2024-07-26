import 'package:flutter/material.dart';

main() {
  runApp(myapp1());
}

class myapp1 extends StatelessWidget {
  const myapp1({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: const Color.fromARGB(255, 96, 96, 96),
        ),
        body: MyWidget(),
      ),
    );
  }
}

class MyWidget extends StatelessWidget {
  const MyWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text("Linux World 12234"),
    );
  }
}
