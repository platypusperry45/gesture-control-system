import DashboardLayout from "../layouts/DashboardLayout";

import PageContainer from "../components/ui/PageContainer";
import SectionHeader from "../components/ui/SectionHeader";

export default function Gestures() {
    return (
        <DashboardLayout>
            <PageContainer>
                <SectionHeader
                    title="Actions"
                    subtitle="Configure gesture mappings."
                />
            </PageContainer>
        </DashboardLayout>
    );
}