import 'package:flutter/material.dart';

class Mybodoy1 extends StatelessWidget {
  const Mybodoy1({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Text("Linux World"),
      width: 100,
      height: 150,
      padding: EdgeInsets.all(10),
      decoration: BoxDecoration(
          color: Color.fromARGB(255, 238, 184, 184),
          border: Border.all(width: 8),
          borderRadius: BorderRadius.circular(5)),
    );
  }
}
