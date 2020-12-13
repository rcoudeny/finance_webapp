import 'package:flutter/material.dart';
import 'package:portfolioTracker/services/authentification_service.dart';
import 'package:portfolioTracker/ui/views/home_view.dart';
import 'package:portfolioTracker/ui/views/sign_in_view.dart';
import 'package:provider/provider.dart';

void main() async {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: AuthentificationWrapper(),
    );
  }
}

class AuthentificationWrapper extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    if (null == null) {
      return HomeView();
    }
    return SignInView();
  }
}
