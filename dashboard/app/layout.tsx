export const metadata = {
  title: 'Drop Intelligence Dashboard',
  description: 'BigQuery-powered intelligence dashboard for Drop',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
