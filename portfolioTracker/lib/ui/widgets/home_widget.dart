import 'package:flutter/material.dart';
import 'package:portfolioTracker/services/api_service.dart';
import 'package:portfolioTracker/ui/base_widget.dart';

class HomeWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
          child: FutureBuilder(
              future: ApiService().fetchTransactions(),
              builder: (BuildContext context, AsyncSnapshot<dynamic> snapshot) {
                switch (snapshot.connectionState) {
                  case ConnectionState.waiting:
                    return Text('Loading....');
                  default:
                    if (snapshot.hasError) {
                      return Text('Error: ${snapshot.error}');
                    } else {
                      Text("Ingelod");
                      // return ExpensesWidget(
                      //   expenseCategory: snapshot.data,
                      // );
                    }
                }
              })),
    );
  }
}
