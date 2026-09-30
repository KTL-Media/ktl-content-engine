import type { GenerationProvider } from "./types";

// Placeholder until a real provider is selected. Fails when the prompt contains "[fail]" so the refund path is testable.
export const stubProvider: GenerationProvider = {
  name: "stub",
  async generate(req) {
    if (req.prompt.includes("[fail]")) throw new Error("stub provider failure");
    const video = req.type.startsWith("animation");
    return {
      provider: "stub",
      modelVersion: "stub-0",
      outputs: [{ kind: video ? "video" : "image", storageKey: `stub/${req.jobId}.${video ? "mp4" : "png"}` }],
    };
  },
};
