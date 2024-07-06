import 'dart:io';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';
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
  List<String> readUsetime(){
    final db = sqlite.sqlite3.open('/home/luca/Luca/Privat/Python/digitalhealth/digitalhealth.db');
    final sqlite.ResultSet usetimes = db.select('SELECT * FROM ${getDate()}');
    var usetimeList = <String>{};
    for (final sqlite.Row row in usetimes) {
      var usetime = row['usetime'].toString();
      usetimeList.add(usetime);
    }
    return usetimeList.toList();
  }
  List<String> readAppName(){
    final db = sqlite.sqlite3.open('/home/luca/Luca/Privat/Python/digitalhealth/digitalhealth.db');
    final sqlite.ResultSet appnames = db.select('SELECT * FROM ${getDate()}');
    var appnameList = <String>{};
    for (final sqlite.Row row in appnames) {
      var appname = row['appname'].toString();
      appnameList.add(appname);
    }
    return appnameList.toList();
  }
}

class AppUsageWidget extends StatelessWidget {
  const AppUsageWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: [
        Expanded(
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: LayoutBuilder(builder: (context, constraints) {
              return PieChart(
                PieChartData(
                  centerSpaceRadius: double.nan,
                  borderData: FlBorderData(show: false),
                  sectionsSpace: 2,
                  sections: piechartSection(),
                ),
              );
            }),
          ),
        ),
        Padding(
          padding: const EdgeInsets.only(left: 30, top: 20, right: 50, bottom: 10),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: generateLegend(),
          ),
        )
      ],
    );
  }

  List<Widget> generateLegend() {
    var appnames = GetData().readAppName();
    return appnames.map((appname) => Text(appname)).toList();
  }

  List<PieChartSectionData> piechartSection() {
    var length = GetData().readUsetime().length;
    var value = GetData().readUsetime();
    var colors = [Colors.blue, Colors.red, Colors.orange, Colors.green, Colors.purple, Colors.yellow];
    return List.generate(
      length,
          (i) {
        return PieChartSectionData(value: double.parse(value[i]), color: colors[i]);
      },
    );
  }// List.generate
}