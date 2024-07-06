import 'dart:io';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:path/path.dart' as p;
import 'package:digital_health/main.dart';

class Settings extends StatelessWidget{
  const Settings({super.key});

  @override
  Widget build(BuildContext context) {
    return SettingsPage();
  }


}

class SettingsPage extends StatefulWidget{
  const SettingsPage({super.key});
  @override
  State<StatefulWidget> createState() => _SettingsPageState();

}

class _SettingsPageState extends State<SettingsPage> {
  String selectedValue = getTheme();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Center(
            child:
            Text(
                style: TextStyle(
                  fontSize: 50,
                ),
                "Settings"),

          ),
          Text("Theme: "),
          DropdownButton(
              value: selectedValue,
              items: dropdownItems,
              onChanged: (String? newValue) {
                setState(() {
                  selectedValue = newValue!;
                  save();
                });
              }),
          SizedBox(height: 20),
        ],
      ),
    );
  }
  List<DropdownMenuItem<String>> get dropdownItems{
    List<DropdownMenuItem<String>> menuItems = [
      DropdownMenuItem(child: Text("dark"),value: "dark"),
      DropdownMenuItem(child: Text("light"),value: "light"),
    ];
    return menuItems;
  }

  void save() {
    var filePath = p.join('/home/luca/Luca/Privat/Python/digitalhealth', 'config.json');
    File file = File(filePath);
    var fileContent = file.readAsStringSync();
    var data = jsonDecode(fileContent);
    data['Theme'] = selectedValue;
    var data2 = json.encode(data);
    MyApp().changeTheme();
    file.writeAsString(data2);
  }
}