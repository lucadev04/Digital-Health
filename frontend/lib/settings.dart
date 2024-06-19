import 'dart:convert';

import 'package:flutter/material.dart';

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
  String selectedValue = "dark";

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
                });
              }),
          SizedBox(height: 20),
          ElevatedButton(
            onPressed: () => save(),
            child: const Text('Save'),
          )
        ],
      ),
    );
  }
  save() {
    //TODO: save data in config.json
    String theme = selectedValue;
  }
  List<DropdownMenuItem<String>> get dropdownItems{
    List<DropdownMenuItem<String>> menuItems = [
      DropdownMenuItem(child: Text("dark"),value: "dark"),
      DropdownMenuItem(child: Text("light"),value: "light"),
    ];
    return menuItems;
  }
}