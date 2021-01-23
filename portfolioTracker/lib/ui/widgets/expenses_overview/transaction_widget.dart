import 'package:flutter/material.dart';
import 'package:portfolioTracker/models/transaction_model.dart';
import 'package:portfolioTracker/models/category_model.dart';

class ExpensesWidget extends StatelessWidget {
  Category expenseCategory;
  ExpensesWidget({this.expenseCategory});

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
        child: Column(
      children: <Widget>[
        Text(expenseCategory.categoryName +
            " Total: " +
            expenseCategory.getTotal().toString()),
        for (var ec in expenseCategory.subCategories)
          ExpensesWidget(expenseCategory: ec),
        for (var expense in expenseCategory.expenses)
          ExpenseWidget(expense: expense)
      ],
    ));
  }
}

class ExpenseWidget extends StatelessWidget {
  Transaction expense;
  ExpenseWidget({this.expense});

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Text(expense.date),
        SizedBox(width: 10),
        Text(expense.amount.toString())
      ],
    );
  }
}
