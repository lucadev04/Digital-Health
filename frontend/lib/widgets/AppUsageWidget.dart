import 'dart:io';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:sqlite3/sqlite3.dart' as sqlite;
import 'package:path/path.dart' as p;

class GetData{
  //here we save
  String getDate(){
    var filePath = p.join('/home/luca/Luca/Privat/Python/digitalhealth', 'config.json');
    File file = File(filePath);
    var fileContent = file.readAsStringSync();
    var data = jsonDecode(fileContent);
    return data['Date'];
  }

  //here we save the appusage and the usetime in a list of maps
  List<Map<String, String>> readAppUsageData(){
    final db = sqlite.sqlite3.open('/home/luca/Luca/Privat/Python/digitalhealth/digitalhealth.db');
    final sqlite.ResultSet results = db.select('SELECT appname, usetime FROM ${getDate()}');

    var appUsageData = <Map<String, String>>[];
    for (final sqlite.Row row in results) {
      appUsageData.add({
        'appname': row['appname'].toString(),
        'usetime': row['usetime'].toString(),
      });
    }
    return appUsageData;
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
    var appUsageData = GetData().readAppUsageData();
    var colors = [Colors.blue, Colors.red, Colors.orange, Colors.green, Colors.purple, Colors.lightBlue, Colors.cyan, Colors.pink, Colors.lightGreen, Colors.deepOrange];

    return appUsageData.asMap().entries.map((entry) {
      int index = entry.key;
      String appname = entry.value['appname']!;

      return Padding(
        padding: const EdgeInsets.symmetric(horizontal: 0),
        child: Row(
          children: [
            Icon(Icons.rectangle, color: colors[index % colors.length]),
            const SizedBox(width: 8),
            Text(appname),
          ],
        ),
      );
    }).toList();
  }

  List<PieChartSectionData> piechartSection() {
    var appUsageData = GetData().readAppUsageData();
    var colors = [Colors.blue, Colors.red, Colors.orange, Colors.green, Colors.purple, Colors.lightBlue, Colors.cyan, Colors.pink, Colors.lightGreen, Colors.deepOrange];

    return List.generate(
      appUsageData.length,
          (i) {
        double usetime = double.parse(appUsageData[i]['usetime']!);
        return PieChartSectionData(value: usetime, color: colors[i % colors.length]);
      },
    );
  }
}
