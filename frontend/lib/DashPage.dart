import 'package:flutter/material.dart';
import 'package:digital_health/widgets/AppUsageWidget.dart';


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
              child: AppUsageWidget(),
            ),
            const Card(),
            const Card()
          ],
        );
      }),
    );
  }
}

