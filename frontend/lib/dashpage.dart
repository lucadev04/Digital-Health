import 'dart:io';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:sqlite3/common.dart';
import 'package:sqlite3/sqlite3.dart' as sqlite;
import 'package:path/path.dart' as p;

class GetData{
  String getDate(){
    var filePath = p.join('/home/luca/Luca/Privat/Python/digitalhealth', 'config.json');
    File file = File(filePath);
    var fileContent = file.readAsStringSync();
    var data = jsonDecode(fileContent);
    return data['Date'];
  }
   List<String> readDatabase(){
    final db = sqlite.sqlite3.open('/home/luca/Luca/Privat/Python/digitalhealth/digitalhealth.db');
    final sqlite.ResultSet usetimes = db.select('SELECT * FROM ${getDate()}');
    var usetimeList = <String>{};
    for (final sqlite.Row row in usetimes) {
      var usetime = row['usetime'].toString();
      usetimeList.add(usetime);
    }
    return usetimeList.toList();
  }
}

class DashPage extends StatelessWidget {
  const DashPage({super.key});


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: LayoutBuilder(builder: (context, constraints) {
        return GridView.count(
          crossAxisCount: constraints.maxWidth < 800 ? 1 : 2,
          childAspectRatio: 1.7,
          padding: const EdgeInsets.all(16),
          crossAxisSpacing: 16,
          mainAxisSpacing: 16,
          children:[
            const Card(
              child: UsetimeWidget(),
            ),
            const Card(),
            const Card()
          ],
        );
      }),
    );
  }
}

class UsetimeWidget extends StatelessWidget {
  const UsetimeWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
        padding: const EdgeInsets.all(16),
        child: LayoutBuilder(builder: (context, constraints) {
          return PieChart(PieChartData(
              centerSpaceRadius: double.nan,
              borderData: FlBorderData(show: false),
              sectionsSpace: 2,
              sections: piechartSection(),
          ));
        }));
  }
  List<PieChartSectionData> piechartSection() {
    var length = GetData().readDatabase().length;
    var value = GetData().readDatabase();
    var i = 0;
    return List.generate(
        length,
            (i) {
              return PieChartSectionData(value: double.parse(value[i+1]),);
            },
    );
  }// List.generate
}