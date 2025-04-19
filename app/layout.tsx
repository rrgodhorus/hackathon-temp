export const metadata = {
  title: 'Next.js Hello World',
  description: 'A basic Next.js Hello World application',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}