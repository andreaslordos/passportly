import { ToastContainer, Flip } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { Game } from "./components/Game";
import React, { useEffect, useState } from "react";
import { Infos } from "./components/panels/Infos";
import { useTranslation } from "react-i18next";
import { InfosFr } from "./components/panels/InfosFr";
import { Settings } from "./components/panels/Settings";
import { useSettings } from "./hooks/useSettings";
import { Worldle } from "./components/Worldle";

function App() {
  const { t, i18n } = useTranslation();

  const [infoOpen, setInfoOpen] = useState(false);
  const [settingsOpen, setSettingsOpen] = useState(false);

  const [settingsData, updateSettings] = useSettings();

  useEffect(() => {
    if (settingsData.theme === "dark") {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, [settingsData.theme]);

  return (
    <>
      <ToastContainer
        hideProgressBar
        position="top-center"
        transition={Flip}
        theme={settingsData.theme}
        autoClose={2000}
        bodyClassName="font-bold text-center"
      />
      {i18n.resolvedLanguage === "fr" ? (
        <InfosFr
          isOpen={infoOpen}
          close={() => setInfoOpen(false)}
          settingsData={settingsData}
        />
      ) : (
        <Infos
          isOpen={infoOpen}
          close={() => setInfoOpen(false)}
          settingsData={settingsData}
        />
      )}
      <Settings
        isOpen={settingsOpen}
        close={() => setSettingsOpen(false)}
        settingsData={settingsData}
        updateSettings={updateSettings}
      />
      <div className="flex justify-center flex-auto dark:bg-slate-900 dark:text-slate-50">
        <div className="w-full max-w-lg flex flex-col">
          <header className="border-b-2 border-gray-200 flex">
            <button
              className="mx-3 text-xl"
              type="button"
              onClick={() => setInfoOpen(true)}
            >
              ❔
            </button>
            <h1 className="text-4xl font-bold uppercase tracking-wide text-center my-1 flex-auto">
              Passp<span className="text-green-600">o</span>rtle
            </h1>
            <button
              className="mx-3 text-xl"
              type="button"
              onClick={() => setSettingsOpen(true)}
            >
              ⚙️
            </button>
          </header>
          <Game settingsData={settingsData} />
          <footer className="flex justify-center text-sm mt-8 mb-1">
            <div>
              <div className="flex justify-center text-sm">
                <a href="https://buymeacoffee.com/lordos"><ul><b>Buy me a coffee :)</b></ul></a>
              </div>
              <div>
                <Worldle />, made for my best friends with ❤️
              </div>
            </div>
          </footer>
        </div>
      </div>
    </>
  );
}

export default App;
