import DashboardLayout from "../layouts/DashboardLayout";

import PageContainer from "../components/ui/PageContainer";
import SectionHeader from "../components/ui/SectionHeader";

export default function Gestures() {
    return (
        <DashboardLayout>
            <PageContainer>
                <SectionHeader
                    title="Analytics"
                    subtitle="Evaluate model performance."
                />
            </PageContainer>
        </DashboardLayout>
    );
}