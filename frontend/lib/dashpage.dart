import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';


class DashPage extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: LayoutBuilder(
          builder: (context, constraints) {
            return GridView.count(
              crossAxisCount: constraints.maxWidth < 800 ? 1 : 2,
              childAspectRatio: 1.7,
              padding: const EdgeInsets.all(16),
              crossAxisSpacing: 16,
              mainAxisSpacing: 16,
              children: [
                Card(
                  child: UsetimeWidget(),
                ),
                Card(),
                Card()
              ],
            );
          }
      ),

    );
  }
}

class UsetimeWidget extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Padding(
        padding: const EdgeInsets.all(30),
        child: PieChart(PieChartData(
            centerSpaceRadius: 100,
            borderData: FlBorderData(show: false),
            sectionsSpace: 2,
            sections: [
              PieChartSectionData(value: 35, color: Colors.blue, radius: 100),
              PieChartSectionData(value: 40, color: Colors.orange, radius: 100),
              PieChartSectionData(value: 55, color: Colors.red, radius: 100),
              PieChartSectionData(value: 70, color: Colors.purple, radius: 100),
            ])
        )
    );
  }
}