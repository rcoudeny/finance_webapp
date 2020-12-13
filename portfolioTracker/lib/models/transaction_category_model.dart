import 'package:portfolioTracker/utils/math_utils.dart';

import 'transaction_model.dart';

class TransactionCategory {
  String categoryName;
  List<TransactionCategory> subCategories = new List<TransactionCategory>();
  List<Transaction> expenses = new List<Transaction>();

  TransactionCategory({this.categoryName, this.subCategories, this.expenses});

  double getTotal() {
    double total = 0;
    subCategories.forEach((subCategory) {
      total += subCategory.getTotal();
    });
    expenses.forEach((expense) {
      total += expense.amount;
    });
    return roundDouble(total, 2);
  }

  factory TransactionCategory.fromJSON(Map<String, dynamic> json) {
    // ExpenseCategory test = ExpenseCategory(categoryName: json["category_name"]);
    return TransactionCategory(
        categoryName: json["name"],
        subCategories: List<TransactionCategory>.from(json['subcategories']
            .map((subCategory) => TransactionCategory.fromJSON(subCategory))
            .toList()),
        expenses: List<Transaction>.from(json['transactions']
            .map((expense) => Transaction.fromJSON(expense))
            .toList()));
  }
}
