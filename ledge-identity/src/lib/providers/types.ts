// Model-agnostic provider interface (PRD §12: no coupling to one image/video model).
export interface ProviderRequest {
  jobId: string;
  identityId: string;
  prompt: string;
  type: "image" | "image_hq" | "upscale" | "animation_5s" | "animation_10s";
  settings: Record<string, unknown>;
}

export interface ProviderResult {
  provider: string;
  modelVersion: string;
  outputs: { kind: "image" | "video"; storageKey: string }[];
}

export interface GenerationProvider {
  name: string;
  generate(req: ProviderRequest): Promise<ProviderResult>;
}
