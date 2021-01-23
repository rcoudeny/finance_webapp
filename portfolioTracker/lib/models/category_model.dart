import 'package:portfolioTracker/utils/math_utils.dart';

import 'transaction_model.dart';

class Category {
  String categoryName;
  List<Category> subCategories = new List<Category>();
  List<Transaction> expenses = new List<Transaction>();

  Category({this.categoryName, this.subCategories, this.expenses});

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

  factory Category.fromJSON(Map<String, dynamic> json) {
    // ExpenseCategory test = ExpenseCategory(categoryName: json["category_name"]);
    return Category(
        categoryName: json["name"],
        subCategories: List<Category>.from(json['subcategories']
            .map((subCategory) => Category.fromJSON(subCategory))
            .toList()),
        expenses: List<Transaction>.from(json['transactions']
            .map((expense) => Transaction.fromJSON(expense))
            .toList()));
  }
}
