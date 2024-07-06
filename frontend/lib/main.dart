import 'dart:io';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:digital_health/DashPage.dart';
import 'package:digital_health/SettingsPage.dart';
import 'package:window_size/window_size.dart';
import 'package:flutter/foundation.dart';
import 'package:path/path.dart' as p;

const double windowWidth = 1280;
const double windowHeight = 768;

void setupWindow() {
  if (!kIsWeb && (Platform.isWindows || Platform.isLinux || Platform.isMacOS)) {
    WidgetsFlutterBinding.ensureInitialized();
    setWindowTitle('Digital Health');
    setWindowMinSize(const Size(100, 100));
    getCurrentScreen().then((screen) {
      setWindowFrame(Rect.fromCenter(
        center: screen!.frame.center,
        width: windowWidth,
        height: windowHeight,
      ));
    });
  }
}

void debugPrintSynchronouslyWithText(String? message, String version,
    {int? wrapWidth}) {
  message = "[${DateTime.now()} - $version]: $message";
  debugPrintSynchronously(message, wrapWidth: wrapWidth);
}

String getTheme(){
  var filePath = p.join('/home/luca/Luca/Privat/Python/digitalhealth', 'config.json');
  File file = File(filePath);
  var fileContent = file.readAsStringSync();
  var data = jsonDecode(fileContent);
  return data['Theme'];
}

void main() {
  setupWindow(); //Only used in Desktop App
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Digital Health',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      darkTheme: ThemeData.dark(),
      themeMode: changeTheme(),
      home: const MyHomePage(),
    );
  }

  changeTheme() {
    var theme = getTheme();
    switch(theme){
      case "dark":
        return ThemeMode.dark;
      case "light":
        return ThemeMode.light;
    }
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _selectedIndex = 0;

  final List<Widget> _pages = [
    const DashPage(),
    const Settings(),
  ];

  void _onDestinationSelected(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: [
          SafeArea(
            child: NavigationRail(
              extended: true,
              destinations: const [
                NavigationRailDestination(
                  icon: Icon(Icons.dashboard),
                  label: Text('Dashboard'),
                ),
                NavigationRailDestination(
                  icon: Icon(Icons.settings),
                  label: Text('Settings'),
                ),
              ],
              selectedIndex: _selectedIndex,
              onDestinationSelected: _onDestinationSelected,
            ),
          ),
          Expanded(
            child: Container(
              color: Theme.of(context).colorScheme.primaryContainer,
              child: _pages[_selectedIndex],
            ),
          ),
        ],
      ),
    );
  }
}

