class Transaction {
  String date;
  double amount;
  String opponent;
  String opponentAccount;
  String comment;
  String ownAccount;

  Transaction(
      {this.date,
      this.amount,
      this.opponent,
      this.opponentAccount,
      this.comment,
      this.ownAccount});

  factory Transaction.fromJSON(Map<String, dynamic> json) {
    return Transaction(
        date: json['date'],
        amount: json['amount'],
        opponent: json['opponent'],
        opponentAccount: json['opponent_account'],
        comment: json['comment'],
        ownAccount: json['own_account']);
  }
}
