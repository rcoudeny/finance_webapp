import 'package:flutter/material.dart';
import 'package:portfolioTracker/models/user_model.dart';
import 'package:portfolioTracker/services/auth_service.dart';
import 'package:portfolioTracker/ui/widgets/authorization/sign_in_widget.dart';
import 'package:portfolioTracker/ui/widgets/home_widget.dart';
import 'package:provider/provider.dart';

void main() async {
  runApp(FinanceApp());
}

class FinanceApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return StreamProvider<User>.value(
        value: AuthService.instance.userStream,
        child: MaterialApp(
          title: 'Finance application',
          debugShowCheckedModeBanner: false,
          theme: ThemeData(
            primarySwatch: Colors.teal,
            visualDensity: VisualDensity.adaptivePlatformDensity,
          ),
          home: AuthentificationWrapper(),
        ));
  }
}

class AuthentificationWrapper extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final user = Provider.of<User>(context);

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.teal,
        toolbarHeight: 80,
      ),
      body: user != null ? HomeWidget() : SignInWidget(),
    );
  }
}
