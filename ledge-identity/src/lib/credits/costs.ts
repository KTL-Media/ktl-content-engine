// Illustrative costs from PRD §13. Configurable; move to DB once pricing is decided.
export const JOB_COSTS = {
  image: 5,
  image_hq: 12,
  upscale: 3,
  identity_reprocess: 25,
  animation_5s: 30,
  animation_10s: 60,
} as const;

export type JobType = keyof typeof JOB_COSTS;

export function jobCost(type: JobType, variations = 1): number {
  if (type === "image") {
    if (variations === 4) return 16; // bundle discount
    if (variations === 2) return 10;
  }
  return JOB_COSTS[type];
}
