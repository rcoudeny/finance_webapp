import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:portfolioTracker/models/transaction_category_model.dart';

import '../constants.dart';

class ApiService {
  static final ApiService _apiService = ApiService._internal();

  factory ApiService() {
    return _apiService;
  }
  ApiService._internal();

  Future<TransactionCategory> fetchTransactions() async {
    var response = await http.get(baseApiUrl + "transactions");
    if (response.statusCode == 200) {
      TransactionCategory ec =
          TransactionCategory.fromJSON(jsonDecode(response.body));
      // print(ec.getTotal());
      return ec;
    } else {
      throw Exception("Failed to load expenses");
    }
    // var expenseFile = File("../../../assets/searchMovement.xls");
    // var stream =
    //     new http.ByteStream(DelegatingStream.typed(expenseFile.openRead()));
    // // get file length
    // // print(stream.first);
    // var length = await expenseFile.length();

    // var uri = Uri.parse(baseApiUrl + 'uploadfile');
    // var request = new http.MultipartRequest("POST", uri);
    // var multipartFile = new http.MultipartFile('file', stream, length,
    //     filename: basename(expenseFile.path));

    // // add file to multipart
    // request.files.add(multipartFile);

    // // send
    // var response = await request.send();
    // print(response.toString());
    // return response;
  }
}
