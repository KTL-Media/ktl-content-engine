import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = { title: "Ledge Identity", description: "Your persistent AI visual identity." };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
