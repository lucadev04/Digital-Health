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
  String readDatabase(){
    final db = sqlite.sqlite3.open('/home/luca/Luca/Privat/Python/digitalhealth/digitalhealth.db');
    final sqlite.ResultSet usetimes = db.select('SELECT * FROM '+getDate());
    var apps = Map<String, String>();
    for (final sqlite.Row row in usetimes) {
      var appname = row['appname'];
      var usetime = row['usetime'].toString();
      apps[appname] = usetime;
    }
    var nemo = apps.values.toList();
    var nemo2 = nemo[2];
    return nemo2;
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
            Card(
              child: UsetimeWidget(),
            ),
            Card(
              child: Text(GetData().readDatabase()),
            ),
            Card()
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
              sections: [
                PieChartSectionData(value: 35, color: Colors.blue),
                PieChartSectionData(value: 40, color: Colors.orange),
                PieChartSectionData(value: 55, color: Colors.red),
                PieChartSectionData(value: 70, color: Colors.purple),
              ]));
        }));
  }
}