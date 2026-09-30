import Link from "next/link";

export default function Home() {
  return (
    <main style={{ maxWidth: 640, margin: "5rem auto", padding: "0 16px" }}>
      <h1>Create once. Be visually recognizable anywhere.</h1>
      <p>A persistent, consent-based AI visual identity for images and video.</p>
      <Link href="/login">Get started</Link>
    </main>
  );
}
