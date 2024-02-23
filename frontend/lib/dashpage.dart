import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';


//https://github.com/imaNNeo/fl_chart/issues/353

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
          children: const [
            Card(
              child: UsetimeWidget(),
            ),
            Card(),
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
          final shortestSide = constraints.smallest.shortestSide;
          return PieChart(PieChartData(
              centerSpaceRadius: 8,
              borderData: FlBorderData(show: false),
              sectionsSpace: 2,
              sections: [
                PieChartSectionData(
                    value: 35, color: Colors.blue, radius: shortestSide / 2),
                PieChartSectionData(
                    value: 40, color: Colors.orange, radius: shortestSide / 2),
                PieChartSectionData(value: 55, color: Colors.red),
                PieChartSectionData(value: 70, color: Colors.purple),
              ]));
        }));
  }
}

/*
 return Padding(
        padding: const EdgeInsets.all(16),
        child: PieChart(PieChartData(
            centerSpaceRadius: double.nan,
            borderData: FlBorderData(show: false),
            sectionsSpace: 2,
            sections: [
              PieChartSectionData(value: 35, color: Colors.blue),
              PieChartSectionData(value: 40, color: Colors.orange),
              PieChartSectionData(value: 55, color: Colors.red),
              PieChartSectionData(value: 70, color: Colors.purple),
            ])));
  }
*/
/*child: LayoutBuilder (
          builder: (context, constraints) {
            final shortestSide = constraints.biggest.shortestSide;
            return PieChart(PieChartData(
            centerSpaceRadius: shortestSide / 2,
            borderData: FlBorderData(show: false),
            sectionsSpace: 2,
            sections: [
              PieChartSectionData(value: 35, color: Colors.blue, radius:  shortestSide / 2 - 16),
              PieChartSectionData(value: 40, color: Colors.orange),
              PieChartSectionData(value: 55, color: Colors.red),
              PieChartSectionData(value: 70, color: Colors.purple),
            ]));
          }
        )*/