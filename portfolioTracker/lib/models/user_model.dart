class User {
  String username;
  String email;
  String token;
  User({this.username, this.email, this.token});

  factory User.fromJSON(Map<String, dynamic> json) {
    return User(
      username: json['username'],
      email: json['email'],
      token: json['token'],
    );
  }
}
