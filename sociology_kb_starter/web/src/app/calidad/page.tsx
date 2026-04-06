import { QualityReportView } from "@/components/quality-report-view";
import { loadQualityReport } from "@/lib/generated-data";

export default async function QualityPage() {
  const report = await loadQualityReport();

  return <QualityReportView report={report} />;
}
