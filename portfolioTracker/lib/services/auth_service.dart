import 'dart:async';
import 'dart:convert';
import 'dart:html';

import 'package:dio/dio.dart';
import 'package:portfolioTracker/models/user_model.dart';
import 'package:http/http.dart' as http;

import '../constants.dart';

class AuthService {
  static final AuthService instance = new AuthService();
  User user;

  User get currentUser {
    return user;
  }

  AuthService() {
    // get token
    this.jwtToken = window.localStorage["jwttoken"];
    checkCurrentUser.then((value) => setJwtToken(user));

    // verify if token is still valid with /user

    // add user on stream
  }

  String jwtToken = '';

  get headers {
    if (jwtToken == null) {
      return {
        "Content-Type": "application/json",
        "Accept": "Application/json",
      };
    }
    if (jwtToken.isEmpty) {
      return {
        "Content-Type": "application/json",
        "Accept": "Application/json",
      };
    } else {
      return {
        "Content-Type": "application/json",
        "Accept": "Application/json",
        "Authorization": "Bearer " + jwtToken
      };
    }
  }

  StreamController<User> userController = StreamController<User>();

  Future<User> get checkCurrentUser async {
    // TODO: Over dio gebruiken voor de http calls?
    final response = await http.get('$baseApiUrl/authentification/currentuser',
        headers: headers);
    if (response.statusCode == 200) {
      User user = User.fromJSON(jsonDecode(response.body));
      return user;
    } else {
      return null;
    }
  }

  Stream<User> get userStream {
    return userController.stream;
  }

  void logout() {
    setJwtToken(null);
  }

  Future<User> login(String email, String password) async {
    var map = new Map<String, dynamic>();
    map['username'] = email;
    map['password'] = password;

    try {
      var dio = Dio();
      FormData formData = new FormData.fromMap(map);
      Response<dynamic> response =
          await dio.post("$baseApiUrl/authentification/signin", data: formData);
      print(response.statusCode);
      if (response.statusCode == 200) {
        User user = User.fromJSON(response.data);
        setJwtToken(user);
        return user;
      } else if (response.statusCode == 401) {
        return null;
      }
    } catch (e) {
      print("Username or password is incorrect.");
    }

    // var json = {"username": "email", "password": "password"};
    // final response = await http.post("$baseApiUrl/authentification/signin",
    //     headers: this.headers, body: jsonEncode(map));
    // if (response.statusCode == 200) {
    //   User user = User.fromJSON(jsonDecode(response.body)['user']);
    //   setJwtToken(user);
    //   return user;
    // }
    // throw (jsonDecode(response.body)['errors']['Error']);
  }

  Future<User> register(String username, String email, String password) async {
    var json = {
      "user": {"username": username, "email": email, "password": password}
    };
    final response = await http.post('$baseApiUrl/users',
        headers: this.headers, body: jsonEncode(json));
    if (response.statusCode == 200) {
      User user = User.fromJSON(jsonDecode(response.body)['user']);
      setJwtToken(user);
      return user;
    }
    throw (jsonDecode(response.body)['errors']['Error']);
  }

  setJwtToken(User user, [String token]) {
    if (user == null) {
      jwtToken = '';
      setUser(null);
      window.localStorage["jwttoken"] = "";
    } else {
      jwtToken = token ?? user.token;
      setUser(user);
      window.localStorage["jwttoken"] = jwtToken;
    }
  }

  setUser(User user) {
    this.user = user;
    userController.add(user);
  }
}
