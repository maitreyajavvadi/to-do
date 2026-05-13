import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="min-h-screen bg-brand-yellow flex flex-col items-center justify-center p-8">
      <div className="max-w-2xl w-full">
        {/* Header */}
        <div className="mb-12">
          <div className="inline-block bg-brand-black text-brand-yellow px-4 py-1 text-xs font-bold mb-6 uppercase tracking-widest">
            Enterprise Task Management
          </div>
          <h1 className="text-7xl font-black text-brand-black leading-none mb-4">
            TASK<br />FLOW.
          </h1>
          <p className="text-xl font-medium text-brand-black max-w-md">
            AI-powered task management for modern teams. Built for professionals
            who ship.
          </p>
        </div>

        {/* CTA */}
        <div className="flex gap-4 flex-wrap">
          <Link href="/login" className="nb-btn-primary text-lg px-8 py-4">
            Get Started →
          </Link>
          <Link href="/register" className="nb-btn-secondary text-lg px-8 py-4">
            Sign Up
          </Link>
        </div>

        {/* Feature pills */}
        <div className="flex flex-wrap gap-3 mt-12">
          {[
            'Kanban Board',
            'AI Task Breakdown',
            'Smart Tagging',
            'Team Workflows',
            'Vercel Native',
          ].map((feat) => (
            <span
              key={feat}
              className="px-3 py-1.5 text-sm font-bold border-3 border-brand-black bg-white shadow-brutal"
            >
              {feat}
            </span>
          ))}
        </div>
      </div>
    </main>
  );
}
