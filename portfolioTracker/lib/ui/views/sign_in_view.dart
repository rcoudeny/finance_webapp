import 'package:flutter/material.dart';
import 'package:portfolioTracker/ui/base_widget.dart';

class SignInView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BaseWidget(builder: (context, sizingInformation) {
      return Scaffold(
        body: Center(
          child: Text("Sign in"),
        ),
      );
    });
  }
}
