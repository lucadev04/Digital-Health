import 'package:flutter/material.dart';
import 'package:sqlite3/sqlite3.dart' as sqlite;
import 'package:digital_health/widgets/AppUsageWidget.dart';

String getUsetime(){
  final db = sqlite.sqlite3.open('/home/luca/Luca/Privat/Python/digitalhealth/digitalhealth.db');
  final sqlite.ResultSet results = db.select('SELECT date, formatted_usetime FROM usetimes');
  for (final sqlite.Row row in results){
    if (row["date"] == GetData().getDate()){
      return row['formatted_usetime'];
    }
  }
  throw Exception('did not find date');
}


class UsetimeWidget extends StatelessWidget {
  const UsetimeWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        padding: const EdgeInsets.all(5),
        decoration: BoxDecoration(
          color: Colors.purple,
          borderRadius: BorderRadius.circular(20),
        ),
          child: Center(
            child: Column(
              mainAxisSize: MainAxisSize.min, // Minimiert den Platz, den die Column einnimmt
              children: [
                const Text(
                  'Usetime:',
                  style: TextStyle(fontSize: 20),
                ),
                Text(
                  getUsetime(), // Die Funktion, die die Usetime zurückgibt
                  style: const TextStyle(fontSize: 60),
                ),
              ],
            ),
        )
      )
    );
  }
  }