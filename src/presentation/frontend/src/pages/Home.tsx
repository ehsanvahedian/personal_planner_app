import Header from "../components/header";
import Panel_preview from "../components/panel_preview";

export default function Home(){
    return(
        <>
            <Header />
            <section>
                <h1 className="leading-14">
                    Give your daily <br />life a great assistant
                </h1>
                <h2 className="text">
                    HABER tracks your transactions, Analyzes them every day and reports to you. <br />
                    Keeps your tasks, reminds you.
                </h2>
                <div className="m-8 flex flex-row justify-center gap-x-5">
                    <a 
                    href="/auth" 
                    className="dark:text-black text-white bg-black dark:bg-white
                        p-3 rounded-3xl px-4 font-bold
                    "
                    >
                        Get started
                    </a>
                    <a 
                    href="/auth" 
                    className="text-white  bg-stone-800/80
                    border border-stone-700
                        p-3 rounded-3xl px-4 font-bold
                    "
                    >
                        Explore workspace
                    </a>
                </div>
                <div className="w-2/3 m-auto">
                    <Panel_preview />
                </div>
            </section>
        </>
    );
}