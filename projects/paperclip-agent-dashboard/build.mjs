import { createPluginBundlerPresets } from "@paperclipai/plugin-sdk/bundlers";
import * as esbuild from "esbuild";

const presets = createPluginBundlerPresets({
  workerEntry: "src/worker.ts",
  manifestEntry: "src/manifest.ts",
  uiEntry: "src/ui/index.tsx",
  outdir: "dist",
  sourcemap: false,
  minify: false,
});

await esbuild.build(presets.esbuild.worker);
await esbuild.build(presets.esbuild.manifest);
if (presets.esbuild.ui) {
  await esbuild.build(presets.esbuild.ui);
}

console.log("Build complete: dist/");
