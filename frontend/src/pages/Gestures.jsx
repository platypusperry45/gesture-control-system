import { useMemo, useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";

import PageContainer from "../components/ui/PageContainer";
import SectionHeader from "../components/ui/SectionHeader";
import GradientButton from "../components/ui/GradientButton";

import GestureGrid from "../components/gestures/GestureGrid";
import GestureSearch from "../components/gestures/GestureSearch";

import useGestures from "../hooks/useGestures";

export default function Gestures() {

    const {
        gestures,
    } = useGestures();

    const [search,setSearch]=useState("");

    const filtered=useMemo(()=>{

        return gestures.filter(g=>

            g.name.toLowerCase()

            .includes(search.toLowerCase())

        );

    },[gestures,search]);

    return(

        <DashboardLayout>

            <PageContainer>

                <SectionHeader

                    title="Gesture Library"

                    subtitle="Manage your AI gesture dataset."

                    action={

                        <GradientButton>

                            Add Gesture

                        </GradientButton>

                    }

                />

                <GestureSearch

                    value={search}

                    onChange={setSearch}

                />

                <GestureGrid

                    gestures={filtered}

                />

            </PageContainer>

        </DashboardLayout>

    );

}